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
</style>
