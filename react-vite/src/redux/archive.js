// ./react-vite/src/redux/archive.js

// Action Types
const DELETE_ARCHIVE = 'archives/DELETE_ARCHIVES'
const SET_USER_ARCHIVES = 'archives/SET_USER_ARCHIVES'

// Action Creators
const deleteArchive = (archive) => ({
    type: DELETE_ARCHIVES,
    archive
})



// Thunks for asynchronous actions
export const fetchArchives = () => async (dispatch) => {
    const response = await fetch('/archives')
    if (response.ok) {
        const data = await response.json();

        console.log("Fetched archives data:", data)
    }
}

export const removeArchive = (archiveId) => async (dispatch) => {
    const response = await fetch(`/archives/${archiveId}`, {
        method: 'DELETE'
    })

    if (response.ok) {
        dispatch(deleteArchive(archiveId))
    } else {
        const errorData = await response.json();
        console.error("Error deleting archive:", errorData)
    }
}


// Initial State
const initialState = {
    archives: {}
}

// Reducer
export default function archiveReducer(state = initialState, action) {
    switch (action.type) {
        case DELETE_SPOT: {
            const newState = { ...state };
            delete newState.Archives[action.archiveId];

        }
    }
}
