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
    <p>I am an Assistant Professor at the Department of Economics and
    Finance in Baruch College's Zicklin School of Business, part of the City
    University of New York (CUNY)</p>
    
    <p>I am an applied microeconomist. My primary fields of interest are
    criminal justice, applied econometrics, and healthcare.</p>
    
    <p>I received a Ph.D. in Economics from Brown University. I have an
    M.A. in Economics from Columbia University and undergraduate degrees
    in Economics and in Mathematics from the University of Utah. For
    other details, see my <a href="/cv/">CV</a>.</p>

    <p>You can reach me at <a href="mailto:mauricio.caceresbravo@baruch.cuny.edu">mauricio.caceresbravo@baruch.cuny.edu</a>.</p>
</div>

<!-- 4 or 5; 7278 -->
<div class="mycol-image-cropper">
    <img src="{{ "/assets/mauricio-rect8.jpg" | relateive_url }}" alt="Mauricio Portrait" class="rounded" >
</div>
</div>
