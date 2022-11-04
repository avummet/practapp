pipeline {
   agent { any }

   environment {
     PY_ENV = /opt/python3.7
     REGISTRY_ENV = "artifcatory.com/python/snapshots"
   }

  stages{
    stage('Install -python'){
       steps{
             curl "nuxus.enterprisedoman.com/reporsitories/python3.7"
             sh '''
                 tar -xzf binaries.tar.gz
                 # add python to agent profile script
                 EXPORT PY_HOME= loocation_of_py
       }
    }
  stage(' Unit - test'){
       steps {
         $PY_ENV/pytest ~/practapp/tests
       }
  }
  stage (' linting'){
  $PY_EMV/pylint ~/practapp/
  }
  stage ('build') {
     script{
         sh '''
            oc process -f ./buildConfig.yml |
            oc-build $REGISTRY_ENV
     }
  }
  stage ('deploy') {
        script {
        sh '''
         oc apply -f ./deployConfig.yaml
        }

  }
  }

post {
     // report success or failure to email dl.
     cleanup ()
}
}
