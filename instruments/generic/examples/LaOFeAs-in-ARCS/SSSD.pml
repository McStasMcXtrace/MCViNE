<?xml version="1.0"?>
<!--
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!
!                                   Jiao Lin
!                      California Institute of Technology
!                        (C) 2008  All Rights Reserved
!
! {LicenseText}
!
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->


<!DOCTYPE inventory>

<inventory>

  <component name="SSSD">

    <property name="ncount">10000</property>
    <property name="buffer_size">10000</property>
<!--
    <property name='overwrite-datafiles'>yes</property>
-->

    <component name="geometer">
      <property name="source">(0,0,0), (0,0,0)</property>
      <property name="sample">(0,0,0.15), (0,0,0)</property>
      <property name="neutron_storage">(0,0,0.15), (0,0,0)</property>
      <property name="detector">(0,0,0.15), (0,0,0)</property>
    </component>

    <facility name="source">neutrons_from_storage</facility>
    <component name="neutrons_from_storage">
      <property name="path">ARCS_neutrons_at_sample</property>
    </component>

    <facility name="sample">LaOFeAs_sample</facility>
    <component name="LaOFeAs_sample">
      <property name="xml">sampleassembly.xml</property>
    </component>

    <component name="neutron_storage">
      <property name="path">neutrons</property>
      <property name="packetsize">10000</property>
    </component>

    <facility name="detector">iqe_monitor</facility>
    <component name="iqe_monitor">
      <property name='max_angle_out_of_plane'>90</property>
      <property name='min_angle_out_of_plane'>-90</property>
      <property name='max_angle_in_plane'>180</property>
      <property name='min_angle_in_plane'>-180</property>

      <property name='filename'>IQE.dat</property>

      <property name="Ei">30</property>

      <property name="Qmin">0</property>
      <property name="Qmax">6.5</property>
      <property name="nQ">130</property>

      <property name="Emin">-29</property>
      <property name="Emax">29</property>
      <property name="nE">116</property>
    </component>

  </component>

</inventory>


<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by XMLMill on Mon Jul 14 13:47:59 2008-->

<!-- End of file -->
