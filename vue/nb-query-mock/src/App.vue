<template>
  <div id="app">
    <!-- Bootstrap container -->
    <div class="container-fluid">
      <!-- Page title -->
      <div class="row mx-4">
        <h1 class="mt-2">Cohort Definition Tool</h1>
        <hr class="mt-0 mb-4" />
      </div>

      <!-- Form fields and results -->
      <div class="row mx-4">
        <!-- Query fields -->
        <div class="col-2" id="query-fields-column">
          <div class="row">
            <h2>Query fields</h2>
          </div>

          <div class="row">
            <form method="post">
              <div class="form-row row">
                <div class="form-group col-md-6"></div>
                <div class="form-group col-md-6"></div>
              </div>
              <button class="btn btn-primary" type="submit">
                Query Metadata
              </button>
            </form>
          </div>
        </div>

        <!-- Query results -->
        <div class="col-10" id="query-results-column">
          <div class="row">
            <h2>Results</h2>
          </div>

          <div class="row d-flex justify-content-center">
            <div class="d-flex align-items-center">
              <h3 style="color: gray">Click 'Query Metadata' for results</h3>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

/*

Author: Jonathan Armoza
Created: 11/4/2021
Purpose: Stylesheet for query prototype

/* Tags */

/* Classes */

/* Card */

.btn-group {
  padding-right: 0.5em;
}
.btn-toolbar {
  padding-right: 0;
}
.card {
  background-color: rgb(242, 242, 242);
  border-radius: 10px;
  color: black;
}
.card-checkbox {
  padding-right: 0;
}
.card-content {
  padding-left: 0;
}
.card-dataset-source {
  color: red;
  font-size: 1em;
}
.card-modality {
  font-size: 1em;
}
.card-text {
  font-size: 1.25em;
}
.card-title {
  font-size: 1.75em;

  /* Ellipsis length truncation */
  max-width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* IDs */

/* Card list */
#card-listbox {
  border: 1em;
  border-color: gray;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  height: 65vh;
  overflow-y: auto;
}

#download-results-button {
  background-color: #0d6efd;
  color: white;
  /* visibility: hidden; */
}

#download-results-link {
  color: white;
  text-decoration: none;
}

#query-controls {
  padding-top: 1em;
  padding-bottom: 1em;
}

/* #query-fields-column {

    margin-right: 1em;
}

#query-results-column {

    margin-left: 1em;
} */

#repo-row {
  padding-bottom: 1em;
}

#results-list-group {
  padding-right: 0;
}

#summary-stats {
  float: right;
}
</style>
