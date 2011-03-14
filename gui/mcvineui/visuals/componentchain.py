# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# view of a component chain
# it contains components and "connectors"
# when click an component, one can edit a component
# when click a "connector", one can insert or append/prepent a component



button_id_formatter_for_component='component-%s'
button_id_formatter_for_insert_before='insert-before-component-%s'



from luban.content import load, select, alert
import luban.content as lc


def createComponentButtonLabelElement(component):
    # when icons are available, add them into the "button"
    # path = 'components/%s/middle-size-icon.png' % name
    # img = lc.image(path=path)
    label = '%s: %s' % (component.componentname, component.__class__.__name__)
    p = lc.paragraph(text=[label])
    return p


def createComponentButton(component, infocus=False, buttonids=[], refresh_config_panel=None):
    'create the button for the given component'
    
    button = lc.document(id=button_id_formatter_for_component % component.id)
    button.Class='component-chain-button'

    labelelem = createComponentButtonLabelElement(component)
    button.add(labelelem)
    
    if infocus:
        button.addClass('selected')

    #
    from mcvineui.visuals import select_one
    selectthisbutton = select_one(button.id, buttonids)
    button.onclick = selectthisbutton + [refresh_config_panel]
    
    button.tip = '%s: click for more details' % component.componentname
    
    return button


def visual(
    instrument=None,
    components=[], refresh_component_configuration_panel=None, component_in_focus=None,
    actorname = None,
    db = None,
    director = None,
    ):
    """
    instrument: id of the instrument which has the component chain
    components: list of component instances
    refresh_component_configuration_panel: action factory that creates an action to refresh component configuration panel give the component. sth like lambda component: ... some action ...
    component_in_focus: the component that is now being focused
    actorname: the actor to deal with events for this visual
    db: db manager
    """
    
    doc = lc.document(id='component-chain-container', title='Component chain')
    sp = doc.splitter(id='component-chain')

    # ids of components
    ids = [c.id for c in components]

    # ids of buttons for components
    buttonids = [button_id_formatter_for_component % id for id in ids]

    # ids of insert buttons for components
    insertbuttonids = [button_id_formatter_for_insert_before % id for id in ids]
        
    for component in components:
        compuid = db.getUniqueIdentifierStr(component)
            
        # button to insert before a component
        insertbuttoncontainer = sp.section()
        insertbutton = lc.button(id=button_id_formatter_for_insert_before%component.id)
        insertbuttoncontainer.add(insertbutton)
        insertbutton.Class='component-chain-insert-button'
        insertbutton.label = '==>'
        insertbutton.tip = 'click to insert component'
        insertbutton.onclick = load(
            actor=actorname, routine='onInsertComponent',
            id = instrument, before=compuid)

        # "button" of a comonent
        infocus = component_in_focus.id == component.id
        refresh_config_panel = refresh_component_configuration_panel(component)
        button = createComponentButton(
            component, 
            infocus=infocus, 
            buttonids = buttonids,
            refresh_config_panel = refresh_config_panel,
            )
        sp.section().add(button)
        continue

    # button to append before a component
    appendbuttoncontainer = sp.section()
    appendbutton = lc.button(id='append-component')
    appendbuttoncontainer.add(appendbutton)
    appendbutton.Class='component-chain-insert-button'
    appendbutton.label = '==>'
    appendbutton.tip = 'click to append component'
    appendbutton.onclick = load(
        actor=actorname, routine='onAppendComponent',
        id = instrument)

    return doc


# version
__id__ = "$Id$"

# End of file 
