<?xml version="1.0"?>
<!--
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
!
!                                   Jiao Lin
!                      California Institute of Technology
!                      (C) 2006-2010  All Rights Reserved
!
! {LicenseText}
!
! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-->

<!DOCTYPE inventory>

<inventory>

    <component name="vulcan-ssd">

        <property name="sequence">['source', 'sample', 'detector']</property>

        <facility name="source">sources/Source_simple</facility>
        <facility name="sample">samples/SampleAssemblyFromXml</facility>
        <facility name="detector">detectorsystem</facility>

        <property name="multiple-scattering">False</property>

        <property name="ncount">10000.0</property>
        <property name="buffer_size">1000</property>

        <property name="overwrite-datafiles">False</property>
        <property name="output-dir">out</property>
        <property name="dump-registry">False</property>

        <component name="source">
            <property name="yh">0.1</property>
            <property name="dist">10.0</property>
            <property name="name">source_simple</property>
            <property name="width">0.0</property>
            <property name="dE">10.0</property>
            <property name="gauss">0.0</property>
            <property name="height">0.0</property>
            <property name="flux">1.0</property>
            <property name="dLambda">0.0</property>
            <property name="radius">0.05</property>
            <property name="Lambda0">0.0</property>
            <property name="E0">60.0</property>
            <property name="xw">0.1</property>
        </component>

        <component name="sample">
            <property name="xml">sampleassembly.xml</property>
        </component>

        <component name="detector">
            <component name="m1">
	      <property name="xwidth">0.1</property>
	      <property name="yheight">0.1</property>
              <property name="tmin">0</property>
              <property name="tmax">1</property>
              <property name="nt">100</property>
	      <property name="filename">m1.h5</property>
	    </component>
            <component name="m2">
	      <property name="xwidth">0.1</property>
	      <property name="yheight">0.1</property>
              <property name="wmin">0</property>
              <property name="wmax">10</property>
              <property name="nw">100</property>
	      <property name="filename">m2.h5</property>
	    </component>
            <component name="m3">
	      <property name="xwidth">0.1</property>
	      <property name="yheight">0.1</property>
              <property name="tmin">0</property>
              <property name="tmax">1</property>
              <property name="nt">100</property>
	      <property name="filename">m3.h5</property>
	    </component>
            <component name="m4">
	      <property name="xwidth">0.1</property>
	      <property name="yheight">0.1</property>
              <property name="wmin">0</property>
              <property name="wmax">10</property>
              <property name="nw">100</property>
	      <property name="filename">m4.h5</property>
	    </component>
            <component name="m5">
	      <property name="xwidth">0.1</property>
	      <property name="yheight">0.1</property>
              <property name="tmin">0</property>
              <property name="tmax">1</property>
              <property name="nt">100</property>
	      <property name="filename">m5.h5</property>
	    </component>
            <component name="m6">
	      <property name="xwidth">0.1</property>
	      <property name="yheight">0.1</property>
              <property name="wmin">0</property>
              <property name="wmax">10</property>
              <property name="nw">100</property>
	      <property name="filename">m6.h5</property>
	    </component>
            <component name="geometer">
                <property name="m1">((-2, 0, 0), (0, 90, 0))</property>
                <property name="m2">((-2, 0, 0), (0, 90, 0))</property>
                <property name="m3">((-1.959, 0.403, 0), (0, 90, 0))</property>
                <property name="m4">((-1.959, 0.403, 0), (0, 90, 0))</property>
                <property name="m5">((-1.959, -0.403, 0), (0, 90, 0))</property>
                <property name="m6">((-1.959, -0.403, 0), (0, 90, 0))</property>
            </component>
        </component>

        <component name="geometer">
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="sample">((0, 0, 10), (0, 0, 0))</property>
            <property name="detector">((0, 0, 10), (0, 0, 0))</property>
            <property name="dump">False</property>
        </component>

    </component>

</inventory>

<!-- version-->
<!-- $Id$-->

<!-- Generated automatically by Renderer on Sat Oct 23 04:21:06 2010-->

<!-- End of file -->
<!-- 
 automatically created by the following command:
 $ vulcan-ssd -h -source=Source_simple -sample=SampleAssemblyFromXml -dump-pml=yes
-->

