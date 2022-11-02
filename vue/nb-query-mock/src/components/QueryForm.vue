<template>
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
              <div class="form-group col-md-6">
                <div class="mb-3">
                  <label class="form-label">Age lower</label>
                  <input
                    type="number"
                    name="age_lower"
                    step="any"
                    class="numberinput form-control"
                  />
                </div>
              </div>
              <div class="form-group col-md-6">
                <div class="mb-3">
                  <label class="form-label">Age upper</label>
                  <input
                    type="number"
                    name="age_upper"
                    step="any"
                    class="numberinput form-control"
                  />
                </div>
              </div>
            </div>
            <div class="mb-3">
              <label class="form-label">Sex</label>
              <select type="sex" class="select form-select">
                <option value selected>All</option>
                <option>female</option>
                <option>male</option>
              </select>
            </div>
            <div class="mb-3">
              <label class="form-label">Modality</label>
              <select type="modality" class="select form-select">
                <option value selected>All</option>
                <option>Diffusion weighted</option>
                <option>EEG</option>
                <option>Flow weighted</option>
                <option>T1 weighted</option>
                <option>T2 weighted</option>
              </select>
            </div>
            <div class="mb-3">
              <label class="form-label">Diagnosis</label>
              <select name="diagnosis" class="select form-select">
                <option value selected>All</option>
                <option>Parkinson's disease</option>
              </select>
            </div>
            <div class="mb-3">
              <label class="form-label">Is control</label>
              <select name="is_control" class="select form-select">
                <option value selected>All</option>
                <option>Control</option>
              </select>
            </div>
            <div class="mb-3">
              <label class="form-label">Num sessions</label>
              <input
                type="numebr"
                name="num_sessions"
                step="any"
                class="numberinput form-control"
              />
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
</template>

<script></script>

<style></style>
