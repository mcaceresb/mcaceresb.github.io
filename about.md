---
layout: page
title: Home
subtitle: About
permalink: /about/
---

<head>
<style>
.mycol-image-cropper {
    width: 30%;
    width: 400px;
    height: 350px;
    position: relative;
    overflow: hidden;
    border-radius: 50%;
    margin-bottom: 18px;
}
img {
    display: inline;
    margin: 0 auto;
    height: 100%;
    width: auto;
    float: right;
}
.mycontainer {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    margin: 0 auto;
}
.mycol-text {
    display: flex;
    flex-direction: column;
    width: 75%;
    padding-right: 24px;
    padding-bottom: 6px;
}
/* text-align: justify; */
.mycol-image {
    width: 25%;
    padding-left: 6px;
}
img {
    max-width: 100%;
    height: auto;
}
@media (max-width: 768px) {
  .mycontainer {
    width: 100%;
    flex-direction: column;
    justify-content: space-between;
  }
  .mycol-text {
      width: 100%;
  }
  .mycol-image-cropper {
      width: 30%;
      width: 250px;
      height: 300px;
      position: relative;
      overflow: hidden;
      border-radius: 50%;
      margin-bottom: 18px;
  }
}
/*
 */
</style>
</head>

<!--
<div class="image-cropper">
    <img src="{{ "/assets/mauricio-square.jpg" | relateive_url }}" class="rounded" />
</div>
-->

<div class="mycontainer">
<div class="mycol-text">
    <p>I'm a Ph.D. candidate in the Department of Economics at Brown University.
    My primary fields of interest are labor, applied econometrics, and crime.</p>

    <p>I have a MA in Economics from Columbia University, and BS in Economics
    and a BS in Mathematics from the University of Utah. I worked as a
    research assistant at the National Bureau of Economic Research for two
    years and at the Yale School of Management for two years. I've also worked
    as a credit risk analyst at Zions Bancorporation in Utah and as a data
    analyst for the Veteran's Administration in Boston.</p>

    <p>I'm on the 2024-2025 job market.</p>
</div>

<!-- 4 or 5; 7278 -->
<div class="mycol-image-cropper">
    <img src="{{ "/assets/mauricio-rect5.jpg" | relateive_url }}" alt="Mauricio Portrait" class="rounded" >
</div>
</div>
